package main

import "fmt"

type Counter map[rune]int

func NewCounter(s string) Counter {
	counter := make(Counter)
	for _, c := range s {
		if _, ok := counter[c]; !ok {
			counter[c] = 1
		} else {
			counter[c]++
		}
	}

	return counter
}

func canConstruct(s string, k int) bool {
	if len(s) < k {
		return false
	}

	if len(s) == k {
		return true
	}
	c := NewCounter(s)
	count := 0
	for _, v := range c {
		if v%2 > 0 {
			count++
		}
	}

	return count <= k
}

func main() {
	fmt.Println(canConstruct("cr", 7))
}
