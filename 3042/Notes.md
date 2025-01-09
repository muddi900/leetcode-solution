# Python
- Simple Solution works well. The time comp seems to be O(N log n). The string slice comparison is the main bottleneck.


# Go

- The same solution is still very efficient, however it is not the fastest solution(335a2074af6cd9039b7fad7482cb7551accfa04d)
- Implemented a trie, as that seems to be a most efficient way to search words(4264272a255b5ec2315ee91dbd68694d563015db). However this seems to only work for prefixes.
- I gave in, and looked at the trie implementation solutions, and they are really slow. You need to reverse the word to make it useful. Restored to brute force.