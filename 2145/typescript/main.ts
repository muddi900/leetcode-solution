function prefixCount(words: string[], pref: string): number {
  let count = 0;

  for (const word of words) {
    if (word.substring(0, pref.length) === pref) {
      count++;
    }
  }

  return count;
}

console.log(prefixCount(["pay", "attention", "practice", "attend"], "at"));
console.log(prefixCount(["leetcode", "win", "loops", "success"], "code"));
