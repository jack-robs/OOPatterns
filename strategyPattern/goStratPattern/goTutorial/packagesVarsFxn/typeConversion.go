package main

import (
    "fmt"
)

func main() {
    var i int = 42
    fmt.Printf("%T %v\n", i, i)
    var f float64 = float64(i)
    fmt.Printf("%T %v\n", f, f)
    var u uint = uint(f)
    fmt.Printf("%T %v\n", u, u)

    //other assy approach
    a := 20
    fmt.Printf("%T %v\n", a, a)
    b := float64(i)
    fmt.Printf("%T %v\n", b, b)
    c := uint(f)
    fmt.Printf("%T %v\n", c, c)
}

    
