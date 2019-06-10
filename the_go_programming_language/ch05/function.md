---
author:
- luixiao1223
title: 函数
---

函数声明
========

``` {.go}
func name(parameter-list) (result-list) {
  body
}
```

example
-------

``` {.go}
func hypot(x,y float64) float64 {
  return math.Sqrt(x*x + y*y)
}
```

同类型可以放在一起
------------------

``` {.go}
func f(i, j, k int, s, t string) {/*...*/}
func f(i int, j int, k int, s string, t string){/*...*/}
```

需要注意点
----------

1.  go 语言没有默认参数的概念，也不能指定参数名
2.  函数类型（具有相同形参列表和返回列表的函数是同种类型）
3.  没有函数体的函数声明，可能是来自于go语言之外的语言实现的。

    ``` {.go}
    package math
    func sin(x float64) float64 // 使用汇编语言实现
    ```

递归
====

多值返回
========

忽略参数
--------

``` {.go}
links, _ := findlines(url)
```

传递参数
--------

``` {.go}
func findLinksLog(url string) ([]string, error) {
  log.Printf("findLinks %s", url)
  return findLinks(url)
}
```

有的函数也接受多返回值函数，作为多参数
--------------------------------------

``` {.go}
log.Println(findLinks(url))
// 和下面的调用等价
links, err := findLinks(url)
log.Println(links, err)
```

裸返回
------

``` {.go}
func CountWordsAndImages(url string) (words, images int, err error) {
  resp, err := http.Get(url)
  if err != nil {
    return
  }
  doc, err := html.Parse(resp.Body)
  resp.Body.Close()
  if err != nil {
    err = fmt.Errorf("parsing HTML: %s", err)
    return
  }
  //(这种匿名返回，会让人很难受，让然误解。所以尽量少用这种返回)
  words, images = countWordsAndImages(doc)
  return
}

func countWordsAndImages(n *html.Node) (words, images int) { /* ... */ }
```

错误
====

这里主要讲错误的处理策略

直接向上一层调用者汇报
----------------------

``` {.go}
resp, err := http.Get(url)
if err != nil {
  return nil, err
}
```

重试若干次再报错退出
--------------------

``` {.go}
func WaitForServer(url string) error {
  const timeout = 1 * time.Minute
  deadline := time.Now().Add(timeout)
  for tries := 0; time.Now().Before(deadline); tries++ {
    _, err := http.Head(url)
    if err == nil {
      return nil // success
    }
    log.Printf("server not responding (%s); retrying...", err)
    time.Sleep(time.Second << uint(tries)) // exponential back-off
  }
  return fmt.Errorf("server %s failed to respond after %s", url, timeout)
}
```

直接终止程序
------------

``` {.go}
// (In function main.)
if err := WaitForServer(url); err != nil {
  fmt.Fprintf(os.Stderr, "Site is down: %v\n", err)
  os.Exit(1)
}
```

应该由主程序来做。不应该由库函数来做。库函数应该报告错误就行了。

``` {.go}
log.Fatalf // 可以实现日志输出
```

某些情况下，只是记录错误信息，然后继续运行
------------------------------------------

``` {.go}
if err := WaitForServer(url); err != nil {
  log.Fatalf("Site is down: %v\n", err)
}
```

直接忽略掉错误
--------------

``` {.go}
dir, err := ioutil.TempDir("", "scratch")
if err != nil {
  return fmt.Errorf("failed to create temp dir: %v", err)
}
// ...use temp dir...
os.RemoveAll(dir) // 这个函数可能会错误，但是这里忽略了处理。
```

函数变量
========

``` {.go}
var f func(int) int
```

注意，函数变量之间不可以比较。所以不能把函数变量作为map的key值。但是函数类型可以和nil比较。

作为参数的函数变量

``` {.go}
func forEachNode(n *html.Node, pre, post func(n *html.Node) string){
  //body
}
```

匿名函数
========

``` {.go}
strings.map(func(r rune) rune {return r+1}, "HAL-9000")
```

闭包的概念
----------

``` {.go}
func squares() func() int {
  var x int
  return func() int {
    x++
    return x * x
  }
}

func main() {
  f := squares()
  fmt.Println(f()) // "1"
  fmt.Println(f()) // "4"
  fmt.Println(f()) // "9"
  fmt.Println(f()) // "16"
}
```

容易出错的地方
--------------

### wrong

``` {.go}
var rmdirs []func()
for _, dir := range tempDirs() {

  os.MkdirAll(dir, 0755)
  rmdirs = append(rmdirs, func() {
    os.RemoveAll(dir) // NOTE: incorrect!
  })
}
```

### right

``` {.go}
var rmdirs []func()
for _, d := range tempDirs() {
  dir := d               // NOTE: necessary!
  os.MkdirAll(dir, 0755) // creates parent directories too
  rmdirs = append(rmdirs, func() {
    os.RemoveAll(dir)
  })
}

// ...do some work...
for _, rmdir := range rmdirs {
  rmdir() // clean up
}
```

变长函数
========

``` {.go}
func sum(vals ...int) int {
  total := 0
  for _, val := range vals {
    total += val
  }
  return total
}
```

等价调用
--------

``` {.go}
fmt.Println(sum(1, 2, 3, 4)) // "10"
// 等价的调用
values := []int{1, 2, 3, 4}
fmt.Println(sum(values...)) // "10"
```

不同类型
--------

``` {.go}
func f(...int) {}
func g([]int) {}
```

延迟函数
========

``` {.go}
func title(url string) error {
  resp, err := http.Get(url)
  if err != nil {
    return err
  }
  // Check Content-Type is HTML (e.g., "text/html; charset=utf-8").
  ct := resp.Header.Get("Content-Type")
  if ct != "text/html" && !strings.HasPrefix(ct, "text/html;") {
    resp.Body.Close() // 调用了一次
    return fmt.Errorf("%s has type %s, not text/html", url, ct)
  }
  doc, err := html.Parse(resp.Body)
  resp.Body.Close() // 调用了一次
  if err != nil {
    return fmt.Errorf("parsing %s as HTML: %v", url, err)
  }

  visitNode := func(n *html.Node) {
    if n.Type == html.ElementNode && n.Data == "title" &&
      n.FirstChild != nil {
      fmt.Println(n.FirstChild.Data)
    }
  }
  forEachNode(doc, visitNode, nil)
  return nil
}
```

defer
-----

``` {.go}
func title(url string) error {
  resp, err := http.Get(url)
  if err != nil {
    return err
  }
  defer resp.Body.Close()
  ct := resp.Header.Get("Content-Type")
  if ct != "text/html" && !strings.HasPrefix(ct, "text/html;") {
    return fmt.Errorf("%s has type %s, not text/html", url, ct)
  }
  doc, err := html.Parse(resp.Body)
  if err != nil {
    return fmt.Errorf("parsing %s as HTML: %v", url, err)
  }
  // ...print doc's title element...
  return nil
}
```

注意
----

1.  defer 没有限制使用次数，执行的时候以调研defer的顺序倒序执行。
2.  defer 语句的求值是在执行defer语句的时候执行。
3.  defer 的执行在return语句之后。

改变返回值结果
--------------

``` {.go}
func double(x int) (result int) {
  defer func() { fmt.Printf("double(%d) = %d\n", x, result) }()// return 后执行打印操作
  return x + x
}
_ = double(4)
// Output:
// "double(4) = 8"
```

``` {.go}
func triple(x int) (result int) {
  defer func() { result += x }()
  return double(x)
}
fmt.Println(triple(4)) // "12" 改变了返回值
```

文件描述符应用
--------------

### 可能会耗尽文件描述符资源

``` {.go}
for _, filename := range filenames {
  f, err := os.Open(filename)
  if err != nil {
    return err
  }
  defer f.Close() // NOTE: risky; could run out of file descriptors
  // ...process f...
}
```

### 更好的方法

``` {.go}
for _, filename := range filenames {
  if err := doFile(filename); err != nil {
    return err
  }
}

func doFile(filename string) error {
  f, err := os.Open(filename)
  if err != nil {
    return err
  }
  defer f.Close()
  // ...process f...
}
```

宕机(panic)
===========

注意
----

1.  宕机会导致程序退出，只有在十分严重的错误情况下才可以宕机。
2.  当发生宕机时，所有的延迟函数以倒序执行，直到回到main函数

    ``` {.go}
    func main() {
      f(3)
    }

    func f(x int) {
      fmt.Printf("f(%d)\n", x+0/x) // panics if x == 0
      defer fmt.Printf("defer %d\n", x)
      f(x - 1)
    }
    ```

    outputs

    ``` {.bash org-language="sh"}
    f(3)
    f(2)
    f(1)
    defer 1
    defer 2
    defer 3
    ```

runtime
-------

runtime包提供了转储栈的方法使程序员可以诊断错误。

``` {.go}
gopl.io/ch5/defer2

func main() {
  defer printStack()
  f(3)
}

func printStack() {
  var buf [4096]byte
  n := runtime.Stack(buf[:], false)
  os.Stdout.Write(buf[:n])
}
```

为什么可以打印出栈，因为go语言的宕机机制可以让延迟函数的执行在栈清理之前调用

恢复
====

recover可以劫持宕机，然后处理之后恢复运行

``` {.go}
func Parse(input string) (s *Syntax, err error) {
  defer func() {
    if p := recover(); p != nil {
      err = fmt.Errorf("internal error: %v", p) // 这里就会恢复，程序不会退出
    }
  }()
  // ...parser... 加入在这里发生宕机
}
```

``` {.go}
func soleTitle(doc *html.Node) (title string, err error) {
  type bailout struct{}
  defer func() {
    switch p := recover(); p {
    case nil:
      // no panic
    case bailout{}:
      // "expected" panic
      err = fmt.Errorf("multiple title elements")
    default:
      panic(p) // unexpected panic; carry on panicking
    }
  }() // 定义了一个函数并调用之这是个匿名函数（延迟调用）

  // Bail out of recursion if we find more than one non-empty title.
  forEachNode(doc, func(n *html.Node) {
    if n.Type == html.ElementNode && n.Data == "title" &&
      n.FirstChild != nil {
      if title != "" {
        panic(bailout{}) // 宕机发生地
      }
      title = n.FirstChild.Data
    }
  }, nil)
  if title == "" {
    return "", fmt.Errorf("no title element")
  }
  return title, nil
}
```
