function karatsuba(num1, num2){

    if(num1 < 10 || num2 < 10){ // Base case if inputs are single digits
        return num1*num2;

    } else {
        let n = Math.max(num1.toString().length, num2.toString().length); // length
        let b = Math.floor(n/2); // splitting

        let power = Math.pow(10, b);

        // Spliting of numbers
        let x1 = Math.floor(num1/power); // left half - 56
        let x0 = num1 % power; // right half - 78

        let y1 = Math.floor(num2/power); // left half - 12
        let y0 = num2 % power; // right half - 34

        // Recursive multiplciation
        let z0 = karatsuba(x0, y0) // 2652
        let z2 = karatsuba(x1, y1) // 672
        let z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0; // 2840

        // final result
        return z2 * Math.pow(10, 2*b) + z1 * power + z0 // 7,006,652
    }
}
console.log(karatsuba(5678, 1234))
