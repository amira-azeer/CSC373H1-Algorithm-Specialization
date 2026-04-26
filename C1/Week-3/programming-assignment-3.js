const fs = require("fs");

function median(arr, low, high) {
  const mid = low + Math.floor((high - low) / 2); // index of the middle element (pivot)

  const value1 = arr[high] > arr[mid];
  const value2 = arr[mid] > arr[low];
  const value3 = arr[low] > arr[high];

  if ((value1 && value2) || (!value1 && !value2)) {
    return mid;
  } else if ((value1 && value3) || (!value1 && !value3)) {
    return high;
  } else {
    return low;
  }
}

function partition(arr, low, high) {
  // values greater on the right, those less on the left
  const pivot = arr[low];
  let i = low + 1;

  for (let j = low + 1; j <= high; j++) {
    if (arr[j] < pivot) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
    }
  }

  [arr[low], arr[i - 1]] = [arr[i - 1], arr[low]];
  return i - 1;
}

function quickSort(arr, low, high, flag = 1) {
  if (low >= high) return 0;

  let p;
  if (flag === 1) p = low;
  else if (flag === 2) p = high;
  else p = median(arr, low, high);

  [arr[low], arr[p]] = [arr[p], arr[low]]; // swap chosen pivot to front (required by Partition spec)

  const pivotFinal = partition(arr, low, high);
  const comparisons = high - low;

  return (
    comparisons +
    quickSort(arr, low, pivotFinal - 1, flag) +
    quickSort(arr, pivotFinal + 1, high, flag)
  );
}

const original = fs
  .readFileSync("QuickSort.txt", "utf8")
  .split("\n")
  .filter(Boolean)
  .map(Number);

const X1 = [...original];
const X2 = [...original];
const X3 = [...original];

const c1 = quickSort(X1, 0, X1.length - 1, 1);
const c2 = quickSort(X2, 0, X2.length - 1, 2);
const c3 = quickSort(X3, 0, X3.length - 1, 3);

console.log("Q1 (first pivot):  ", c1);
console.log("Q2 (last pivot):   ", c2);
console.log("Q3 (median pivot): ", c3);

