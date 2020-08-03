package main

import (
	"bufio"
	"fmt"
	"os"
)

func urlify(str []rune) string {
	var queue []rune

	for i := 0; i < len(str)-2; i++ {
		if len(queue) > 0 {
			queue = append(queue, str[i])
			str[i] = queue[0]
			queue = queue[1:]
		}
		if str[i] != rune(' ') {
			continue
		}
		str[i] = '%'
		queue = append(queue, str[i+1])
		queue = append(queue, str[i+2])
		str[i+1] = '2'
		str[i+2] = '0'
		i += 2
	}
	if len(queue) > 0 {
		str[len(str)-2] = queue[0]
	}
	if len(queue) > 1 {
		str[len(str)-1] = queue[1]
	}

	return string(str)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	rawStr, _ := reader.ReadString(',')
	rawStr = rawStr[:len(rawStr)-1] // trim ',' character

	fmt.Println(urlify([]rune(rawStr)))
}
