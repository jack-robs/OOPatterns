package main

import "fmt"

var i, j int = 1, 2

func main() {
    //if init'd, type is implied
    var c, python, java = true, false, "no!"
    fmt.Println(i, j, c, python, java)
    }
