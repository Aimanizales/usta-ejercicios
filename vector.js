const v = [5, -2, 9, -8, 14];
let tmp;

for (let i = 0; i<= 4; i = i + 1) {
    // console.log('i:', i)
    for (j = i + 1;j <= 3;j = j + 1){
        // console.log('j:', j)
        if (v[i] > v[j]) {
            tmp = v[i]
            console.log('tmp = ', tmp)
            v[i] = v[j]
            console.log(`v[${i}] = ${v[i]}`)
            v[j] = tmp
            console.log(`v[${j}] =  ${v[j]}`)
        }
    }
}