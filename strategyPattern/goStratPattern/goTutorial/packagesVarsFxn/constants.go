package main

import "fmt"

//can't use :=
const Pi = 3.14

func main() {
    const World = "hello"
    fmt.Println("Hello", World)
    fmt.Println("Happy", Pi, "day")

    const Truth = true
    fmt.Println("Go rules?", Truth)
}
