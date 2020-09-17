package main

import "fmt"

func main() {
    var i int
    j := i
    fmt.Printf("%T %v, %T %v\n", i, i, j, j)

    //implied types
    a := 42
    fmt.Printf("%T %v\n", a, a)
    b := 3.142
    fmt.Printf("%T %v\n", b, b)
    c := 0.867 + 0.51i
    fmt.Printf("%T %v\n", c, c)
}


