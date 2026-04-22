const fs = require("fs");

const arr = fs.readFileSync("IntegerArray.txt", "utf8")
    .trim()
    .split("\n")
    .map(Number);

function countInversions(arr) {
  const temp = new Array(arr.length);

  function sortAndCount(left, right) {
    if (left >= right) return 0;

    const mid = Math.floor((left + right) / 2);

    let invCount = 0;

    invCount += sortAndCount(left, mid);
    invCount += sortAndCount(mid + 1, right);
    invCount += merge(left, mid, right);

    return invCount;
  }

  function merge(left, mid, right) {
    let i = left;
    let j = mid + 1;
    let k = left;
    let invCount = 0;

    while (i <= mid && j <= right) {
      if (arr[i] <= arr[j]) {
        temp[k++] = arr[i++];
      } else {
        temp[k++] = arr[j++];
        invCount += mid - i + 1;
      }
    }

    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (let x = left; x <= right; x++) {
      arr[x] = temp[x];
    }

    return invCount;
  }

  return sortAndCount(0, arr.length - 1);
}

console.log('Inversion Count', countInversions(arr));
