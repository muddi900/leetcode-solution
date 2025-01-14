function findThePrefixCommonArray(A: number[], B: number[]): number[] {
  const n = A.length;
  const ans: number[] = [];
  const freq: number[] = new Array(n + 1);
  let count = 0;

  for (let i = 0; i < n; i++) {
    const a = A[i], b = B[i];

    freq[a] = (freq[a] || 0) + 1;
    if (freq[a] === 2) {
      count++;
    }

    freq[b] = (freq[b] || 0) + 1;

    if (freq[b] === 2) {
      count++;
    }

    ans.push(count);
  }

  return ans;
}

let A = [1, 3, 2, 4], B = [3, 1, 2, 4];

console.log(findThePrefixCommonArray(A, B));

A = [2, 3, 1], B = [3, 1, 2];

console.log(findThePrefixCommonArray(A, B));
