package main

import (
	"fmt"
	"math"
	"slices"
)

func myAtoI(s string) int {
	var m int64 = 1
	var ans int64 = 0
	flag := false

	// p := len(s) - 1

	for _, c := range s {
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
				ans *= 10
				ans += int64(c - '0')
			}

			if !isNum {
				break
			}
		}
	}

	if ans >= math.MaxInt32 {
		if m == -1 {
			return math.MinInt32
		}

		return math.MaxInt32
	}

	return int(m * ans)
}

func main() {
	// fmt.Println(myAtoI("42"))
	// fmt.Println(myAtoI(" -042"))
	// fmt.Println(myAtoI("1337c0d3"))
	// fmt.Println(myAtoI("0-1"))
	fmt.Println(myAtoI("9223372036854775808"))
}
