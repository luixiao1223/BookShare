/*
  非递归，比较当前文件夹内的文件是否有重复文件。利用的方法是对每一个文件生一个md5 key，然后比较是否有两个文件的md5 key相同。相同就意味着文件重复。
*/
package main

import "fmt"
import "io"
import "io/ioutil"
import "crypto/md5"
import "encoding/hex"
import "os"
import "sync"

type md5Info struct {
	key  string
	name string
}

var token = make(chan struct{}, 100) // 只能同时打开100个文件

var md5map = make(map[string]([]string))

func hash_file_md5(filePath string) (string, error) {
	var returnMD5String string
	file, err := os.Open("./" + filePath)
	if err != nil {
		fmt.Println(err)
		return returnMD5String, err
	}

	defer file.Close()

	hash := md5.New()

	if _, err := io.Copy(hash, file); err != nil {
		return returnMD5String, err
	}

	hashInBytes := hash.Sum(nil)[:16]
	returnMD5String = hex.EncodeToString(hashInBytes)

	return returnMD5String, nil
}

func worker(name string, keychan chan<- md5Info, wg *sync.WaitGroup) {
	token <- struct{}{} // 让打开的文件数量降低到一定范围内。
	key, err := hash_file_md5(name)
	<-token
	defer wg.Done()

	if err != nil {
		return
	}

	var info md5Info
	info.key = key
	info.name = name
	keychan <- info
}

func getinfo(keychan <-chan md5Info, wg *sync.WaitGroup) {

	for info := range keychan {
		vec, flag := md5map[info.key]
		if !flag {
			var nvec = []string{}
			nvec = append(nvec, info.name)
			md5map[info.key] = nvec
		} else {
			md5map[info.key] = append(vec, info.name)
		}
	}

	wg.Done()
}

func main() {
	path := "."
	entries, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Println("Open Dir " + path + " error")
		return
	}

	keychan := make(chan md5Info, 20)
	var wg sync.WaitGroup

	for _, entry := range entries {
		if !entry.IsDir() {
			name := entry.Name()
			wg.Add(1)
			go worker(name, keychan, &wg)
		}
	}

	go func(wg *sync.WaitGroup) {
		wg.Wait()
		close(keychan)
	}(&wg)

	var gg sync.WaitGroup
	gg.Add(1)
	go getinfo(keychan, &gg)

	gg.Wait()
	fmt.Println("----------------------")
	for key, vec := range md5map {
		if len(vec) >= 2 {
			fmt.Println("T:" + key)
			for _, name := range vec {
				fmt.Println("--->", name)
			}
		}
	}
}
