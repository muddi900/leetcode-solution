package main

import (
	"fmt"
	"math"
	"slices"
)

func myAtoI(s string) int {
	m := 1
	ans := 0
	flag := false

	p := len(s) - 1

	for i, c := range s {
		isNum := '0' <= c && c <= '9'

		if !flag {
			if !(isNum || slices.Contains([]rune{'+', '-', ' '}, c)) {
				return 0
			}

			if c == ' ' {
				continue
			}

			if c == '-' || c == '+' {
				if c == '-' {
					m = -1
				}
				flag = true
				continue
			}

			if isNum {
				flag = true
			}
		}

		if flag {
			if isNum {
				ans += int(c-'0') * int(math.Pow10(p-i))
			}

			if !isNum {
				ans /= int(math.Pow10(len(s) - i))
				break
			}
		}
	}

	if ans >= int(math.Pow(2, 31)) {
		if m == -1 {
			return -int(math.Pow(2, 31))
		}

		return int(math.Pow(2, 31)) - 1
	}

	return m * ans
}

func main() {
	// fmt.Println(myAtoI("42"))
	// fmt.Println(myAtoI(" -042"))
	// fmt.Println(myAtoI("1337c0d3"))
	// fmt.Println(myAtoI("0-1"))
	fmt.Println(myAtoI("20000000000000000000"))
}
