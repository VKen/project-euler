function multiplesOf3and5(number=20000) {
  let result = Array.from(Array(number).keys()).reduce((acc, i) => {
    if (i % 3 == 0 || i % 5 == 0 ){
      return acc + i;
    }
    return acc;
  })
  return result;
}

function timeIt(func) {
  let start = performance.now();
  func();
  console.log(`Time to run ${func.name} is ${performance.now() - start} milliseconds`);
}

timeIt(multiplesOf3and5);
