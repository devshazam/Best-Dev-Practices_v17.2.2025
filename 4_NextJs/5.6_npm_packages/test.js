function solution(input, markers) {
    // input = 'bab'
    // markers[0] = 'a'; 
    console.log(input)
    const regex = new RegExp(markers[0]);
    let ii = input.replace(regex, "#");
console.log(markers[1] == '$')
let iii;
    if(markers[1] == '$'){
      iii = ii.replace(/\$/, '#')
    }else{
      const regex2 = new RegExp(markers[1]);
      let iii = ii.replace(regex2, "#");
    }
     
    
     

    console.log(iii)
    let iiii = iii.replace(/\s#.*\n?/,"\n").replace(/\s#.*(\n)?/,""); 

    console.log(iiii)
    return iiii
  };

  solution("a #b\nc\nd $e f g", ["#", "$"], "apples, plums\npears\noranges")
  // , ["@", "-"], "Q\nu\ne"
  