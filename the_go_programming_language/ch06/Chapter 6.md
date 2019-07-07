## 方法

### 6.1 方法声明

#### 方法的声明和普通函数的声明类似，只是在函数名字前面多了一个参数

```
package geometry

import "math"

type Point struct{ X, Y float64 }

// traditional function
func Distance(p, q Point) float64 {
    return math.Hypot(q.X-p.X, q.Y-p.Y)
}

// same thing, but as a method of the Point type
func (p Point) Distance(q Point) float64 {
    return math.Hypot(q.X-p.X, q.Y-p.Y)
}
```

- 附加的参数p 称为方法的接收者
- Go 语言中，接收者不使用特殊名（比如this 或者self ）；而是我们自己选择接收者名字
- 调用方法的时候，接收者在方法名的前面，这样就和声明保持一致

```
p := Point{1, 2}
q := Point{4, 6}
fmt.PrintIn(Distantce(p, q)) // "5", 函数调用
fmt.PrintIn(p.Distantce(q)) // "5", 函数调用
```

- 因为每一个类型有它自己的命名空间，所以我们能够在其他不同的类型中使用名字 Distance 作为方法名

```
// A Path is a journey connecting the points with straight lines.
type Path []Point

// Distance returns the distance traveled along the path.
func (path Path) Distance() float64 {
	sum := 0.0
	for i := range path {
		if i > 0 {
			sum += path[i-1].Distance(path[i])
		}
	}
	return sum
}
```

- Go 和许多其他面向对象的语言不同，它可以将方法绑定到任何类型上。可以很方便地为简单的类型（如数字、字符串、slice 、map ，甚至函数等）定义附加的行为。同一个包下的任何类型都可以声明方法，只要它的类型既不是指针类型也不是接口类型。

```
package main

import (
	"fmt"
)

type Greeting func(name string) string

func (p Greeting) Print(v string) {
	fmt.Println(v)
}

func main() {
	var f Greeting

	f.Print("this is fine")
}
```

- 使用方法的第一个好处：命名可以比函数更简短。在包的外部进行调用的时候，方法能够使用更加简短的名字且省略包的名字：

```
import "gopl.io/ch6/geometry"

perim := geometry.Path{{l, 1}, {5, 1}, {5, 4}, {1, 1}}
fmt.Println(geometry.PathDistance(perim)) //"12"，独立函数
fmt.Println(perim.Distance()) //"12"geometry.Path 的方法
```

### 6.2 指针接收者的方法
#### 由于主调函数会复制每一个实参变量，如果函数需要更新一个变量，或者如果一个实参太大而我们希望避免复制整个实参，因此我们必须使用指针来传递变量的地址。

```
func (p *Point) ScaleBy(factor float64) {
    p.X *= factor
    p.Y *= factor
}
// 注：在真实的程序中，习惯上遵循如果Point 的任何一个方法使用指针接收者，那么所有的 Point 方法都应该使用指针接收者
```

- 命名类型（Point）与指向它们的指针（*Point）是唯一可以出现在接收者声明处的类型。而且，为防止混淆，不允许本身是指针的类型进行方法声明：

```
type P *int
func (P) f() { /* ... */ } // compile error: invalid receiver type
```

- 通过提供 \*Point 能够调用 (*Point).ScaleBy 方法，比如：

```
r := &Point{1, 2}
r.ScaleBy(2)
fmt.Println(*r) // "{2, 4}"

// 或者：
p := Point{1, 2}
pptr := &p
pptr.ScaleBy(2)
fmt.Println(p) // "{2, 4}"

// 或者：
p := Point{1, 2}
(&p).ScaleBy(2)
fmt.Println(p) // "{2, 4}"

// 或者：
p.ScaleBy(2)

// 或者：
pptr.Distance(q)

// 错误：
Point{1, 2}.ScaleBy(2) // compile error: can't take address of Point

```

- 总结：三种合法情况
   1. 实参和形参类型相同
   2. 实参类型为 T 而形参为 *T
   3. 实参类型为 *T 而形参为 T
   
#### 指针类型接受者和非指针类型接受者的区别

```
package main

import "fmt"

type Mutatable struct {
	a int
	b int
}

func (m Mutatable) StayTheSame() { // m是传值传到StayTheSame中来的。所以这个函数中m是调用StayTheSame的变量的一个拷贝
	m.a = 5
	m.b = 7
}

func (m *Mutatable) Mutate() { // m 是调用Mutate的m的一个指针，这是一个巨大的区别
	m.a = 10
	m.b = 14
}

func main() {
	m := &Mutatable{0, 0}
	fmt.Println(m)
	m.StayTheSame()
	fmt.Println(m)
	m.Mutate()
	fmt.Println(m)

	fmt.Println("-----------")

	n := Mutatable{0, 0}
	fmt.Println(n)
	n.StayTheSame()
	fmt.Println(n)
	n.Mutate()
	fmt.Println(n)
}
```

#### nil 是一个合法的接收者

示例：net/url包里 Values 类型定义的一部分

net/url
```
package url

// Values maps a string key to a list of values.
type Values map[string][]string
// Get returns the first value associated with the given key,
// or "" if there are none.
func (v Values) Get(key string) string {
     if vs := v[key]; len(vs) > 0 {
         return vs[0]
     }
     return ""
}
// Add adds the value to key.
// It appends to any existing values associated with key.
func (v Values) Add(key, value string) {
    v[key] = append(v[key], value)
}
```

gopl.io/ch6/urlvalues
```
m := url.Values{"lang": {"en"}} // direct construction
m.Add("item", "1")
m.Add("item", "2")

fmt.Println(m.Get("lang")) // "en"
fmt.Println(m.Get("q"))    // ""
fmt.Println(m.Get("item")) // "1"      (first value)
fmt.Println(m["item"])     // "[1 2]"  (direct map access)

m = nil
fmt.Println(m.Get("item")) // ""
m.Add("item", "3")         // panic: assignment to entry in nil map
```

### 6.3 通过结构体内嵌组成类型

gopl.io/ch6/coloredpoint
```
import "image/color"
type Point struct{ X, Y float64 }
type ColoredPoint struct {
    Point
    Color color.RGBA
}
```

- 內嵌可以使我们在定义 ColoredPoint 时得到一种句法上的简写形式

```
var cp ColoredPoint
cp.X = 1
fmt.Println(cp.Point.X) // "1"
cp.Point.Y = 2
fmt.Println(cp.Y) // "2"
```

- 我们能够通过类型为 ColoredPoint 的接收者调用内嵌类型 Point 的方法，即使在 ColoredPoint 类型没有声明过这个方法：

```
red := color.RGBA{255, 0, 0, 255}
blue := color.RGBA{0, 0, 255, 255}
var p = ColoredPoint{Point{1, 1}, red}
var q = ColoredPoint{Point{5, 4}, blue}
fmt.Println(p.Distance(q.Point)) // "5"
p.ScaleBy(2)
q.ScaleBy(2)
fmt.Println(p.Distance(q.Point)) // "10"
```

- 注意： 这里 Point 类型并不能理解为是 ColoredPoint 类型的基类。Distance 有一个形参 Point, q 不是 Point ，因此虽然 q 有一个内嵌的 Point 字段，但是必须显式地使用它

```
p.Distance(q) // compile error: cannot use q (ColoredPoint) as Point
```

- 匿名字段类型可以是个指向命名类型的指针

```
type ColoredPoint struct {
    *Point
    Color color.RGBA
}

p := ColoredPoint{&Point{1, 1}, red}
q := ColoredPoint{&Point{5, 4}, blue}
fmt.Println(p.Distance(*q.Point)) // "5"
q.Point = p.Point                 // p and q now share the same Point
p.ScaleBy(2)
fmt.Println(*p.Point, *q.Point) // "{2 2} {2 2}"
```

- 当编译器处理选择子（比如 p.ScaleBy）的时候，首先，它先查找到直接声明的方法 ScaleBy ，之后再从来自 ColoredPoint 的内嵌字段的方法中进行查找，再之后从Point 和 RGBA 中内嵌字段的方法中进行查找，以此类推

- 方法只能在命名的类型（比如 Point ）和指向它们的指针（*Point ）中声明，但内嵌帮助我们能够在未命名的结构体类型中声明方法。

```
var (
    mu sync.Mutex // guards mapping 包级别变量
    mapping = make(map[string]string) // 包级别变量
)

func Lookup(key string) string {
    mu.Lock()
    v := mapping[key]
    mu.Unlock()
    return v
}
```

```

var cache = struct {
         sync.Mutex
         mapping map[string]string 
}{mapping: make(map[string]string),} // 匿名结构体变量(ps:struct 没有名字，只使用了一次)
         
func Lookup(key string) string {
         cache.Lock()
         v := cache.mapping[key]
         cache.Unlock()
         return v
}
```

### 6.4 方法变量与表达式

#### 方法变量：选择子 p. Distance 可以赋予一个方法变量，它是一个函数，把方法( Point.Distance ）绑定到一个接收者 p 上

```
p := Point{1, 2}
q := Point{4, 6}

distanceFromP := p.Distance        // method value
fmt.Println(distanceFromP(q))      // "5"
var origin Point                   // {0, 0}
fmt.Println(distanceFromP(origin)) // "2.23606797749979", sqrt(5)

scaleP := p.ScaleBy // method value
scaleP(2)           // p becomes (2, 4)
scaleP(3)           //      then (6, 12)
scaleP(10)          //      then (60, 120)
```

#### 方法表达式：和调用一个普通的函数不同，在调用方法的时候必须提供接收者，并且按照选择子的语法进行调用
```
p := Point{1, 2}
q := Point{4, 6}

distance := Point.Distance   // method expression
fmt.Println(distance(p, q))  // "5"
fmt.Printf("%T\n", distance) // "func(Point, Point) float64"

scale := (*Point).ScaleBy
scale(&p, 2)
fmt.Println(p)            // "{2 4}"
fmt.Printf("%T\n", scale) // "func(*Point, float64)"
```

### 6.5 示例：位向量

fixme

### 6.6 封装
#### Go 语言只有一种方式控制命名的可见性：定义的时候，首字母大写的标识符是可以从包中导出的，而首字母没有大写的则不导出。
- 结论1： 要封装一个对象，必须使用结构体。
示例种的 IntSet 类型被声明为结构体但是它只有单个字段：

```
type IntSet struct {
    words []uint64
}
```

而另一种定义则允许其他包内的使用方读取和改变这个 slice
```
type IntSet []uint64
```

- 结论2： 在Go 语言中封装的单元是包而不是类型.

```
package test

type Kkk struct {
	private string
	Public  string
}
```

```
package main

import (
	"./test"
	"fmt"
)

type some struct {
	words string
}

func main() {
	var fine = test.Kkk{}
	var good = some{}
	//fmt.Println(fine.private) // 不能访问其他包中结构体中的小写开头变量
	fmt.Println(fine.Public) // 可以访问其他包中结构体中的大写开头变量
	good.words = "long"
	fmt.Println(good.words) // 可以访问本包结构体中的小写开头变量
}
```

- 封装提供了三个优点
   1. 因为使用方不能直接修改对象的变量，所以不需要更多的语句用来检查变量的值。
   2. 隐藏实现细节可以防止使用方依赖的属性发生改变，使得设计者可以更加灵活地改变 API 的实现而不破坏兼容性。
   3. 防止使用者肆意地改变对象内的变量。

```
package log
type Logger struct {
    flags  int
    prefix string
    // ...
}
func (l *Logger) Flags() int
func (l *Logger) SetFlags(flag int)
func (l *Logger) Prefix() string
func (l *Logger) SetPrefix(prefix string)
```

- 封装并不总是必须的，比如
```
const day = 24 * time.Hour //day is a time.Duration
fmt.Println(day.Seconds()) // "86400"
```
