package main

import "fmt"

func main() {
    var i, j int = 1, 2
    //instead of var k int = 1
    // := only allowed for var assy in functions
    k := 3
    c, python, java := true, false, "no!"

    fmt.Println(i, j, k, c, python, java)
}
