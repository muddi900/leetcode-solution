function minimumLengthMap(s: string): number {
  if (s.length <= 2) {
    return s.length;
  }
  const counter = new Map();

  for (const char of s) {
    counter.set(char, (counter.get(char) || 0) + 1);
  }

  let min_size = s.length;

  for (const [_, freq] of counter.entries()) {
    if (freq <= 2) {
      continue;
    }

    if (freq % 2 === 0) {
      min_size -= freq - 2;
      continue;
    }

    min_size -= freq - 1;
  }

  return min_size;
}

function minimumLengthMemo(s: string): number {
  if (s.length <= 2) {
    return s.length;
  }
  const counter = new Array<number>(26);

  for (const char of s) {
    const index = char.codePointAt(0)! - "a".codePointAt(0)!;
    counter[index] = (counter[index] || 0) + 1;
  }

  let min_size = s.length;

  for (const freq of counter) {
    if (!freq || freq <= 2) {
      continue;
    }

    if (freq % 2 === 0) {
      min_size -= freq - 2;
      continue;
    }

    min_size -= freq - 1;
  }

  return min_size;
}

console.log(minimumLengthMemo("abaacbcbb"));
console.log(minimumLengthMemo("aa"));

Deno.bench("Map", () => {
  minimumLengthMap("abaacbcbb");
  minimumLengthMap("aa");
  minimumLengthMap(
    "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj",
  );
});

Deno.bench("Memo", () => {
  minimumLengthMemo("abaacbcbb");
  minimumLengthMemo("aa");
  minimumLengthMemo(
    "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj",
  );
});
