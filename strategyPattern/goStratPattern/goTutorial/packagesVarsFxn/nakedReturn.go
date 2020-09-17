package main

import "fmt"

//retuns x, y in that order
func split(sum int) (x , y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

func main() {
    fmt.Println(split(17))
}
