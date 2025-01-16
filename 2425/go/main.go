package main

import "fmt"

func xorAllNums(nums1 []int, nums2 []int) int {
	x1 := 0
	x2 := 0

	n1 := len(nums1)
	n2 := len(nums2)

	if n2%2 > 0 {
		for _, n := range nums1 {
			x1 ^= n
		}
	}

	if n1%2 > 0 {
		for _, n := range nums2 {
			x2 ^= n
		}
	}

	return x1 ^ x2
}

func main() {
	fmt.Println(xorAllNums([]int{2, 1, 3}, []int{10, 2, 5, 0}))
	fmt.Println(xorAllNums([]int{1, 2}, []int{3, 4}))
}
