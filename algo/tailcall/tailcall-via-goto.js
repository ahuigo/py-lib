function underscore(s){
    return '__'+s
}

const alignRightBlank = '    '
function alignRight(code){
    return code.replaceAll('\n','\n    ')
}

function transform(name, args, body) {
    // 将参数提取出来，成为迭代变量
    var args = args
    
    //原来的参数则用来初始化迭代变量
    var init_var = args.map(function (arg) { return 'let ' + arg + ' = ' + underscore(arg) + ';\n' }).join('');
    
    // 创建一个迭代函数，迭代函数只用来只用来更新迭代变量
    var iterate_name = underscore(name);
    var loop_name = iterate_name + '_loop';
    var init_iterate
        = 'function ' + iterate_name + '(' + args.map(underscore).join(', ') + ') {\n'
        + (args.map(function (arg) { return arg + ' = ' + underscore(arg) + ';'; }).join('\n'))
        + '\n}\n';

    var new_body
        = init_var
        + init_iterate
        
        // 将原来函数的里面所代码（不包括我们上面的迭代函数和迭代变量初始化）包在一个 while (true) 迭代循环里面
        + loop_name + ': while (true) {\n'

        // 递归终止的 return 不变，尾递归的 return 替换成迭代函数，并且 continue 掉上面的迭代循环
        + (
          body.replace(
            new RegExp('return\\s+' + name + '(.*?)(;|\n)', 'g')
            , iterate_name + '$1' + '$2' + ' continue ' + loop_name + ';'
          )
        )
        + '\n}';

    // 将函数包装起来
    var code
        = 'function ' + name + '(' + args.map(underscore).join(', ') + ') {'
        + alignRight('\n'+new_body)
        + '\n};' +name;
      return (code);
}


function getFuncParams(func) {
    const STRIP_COMMENTS = /((\/\/.*$)|(\/\*[\s\S]*?\*\/))/mg;
    const ARGUMENT_NAMES = /([^\s,]+)/g;
    const fnStr = func.toString().replace(STRIP_COMMENTS, '');
    const result = fnStr.slice(fnStr.indexOf('(')+1, fnStr.indexOf(')')).match(ARGUMENT_NAMES);
      if(result === null)
         result = [];
      return result;
}

function getFuncBody(fn){
    const code = fn.toString(); 
    return code.slice(code.indexOf("{") + 1, code.lastIndexOf("}"));
}

function fact(n, r) { 
    if (n <= 0) {
        return 1 * r; 
    } else {
        return fact(n - 1, r * n); 
    }
}

const name = fact.name
const params = getFuncParams(fact)
const body = getFuncBody(fact)

const tailFactCode = transform(name, params, body)
console.log('generate tailfact:\n',tailFactCode)
const tailFact = eval(tailFactCode)

console.log(tailFact(7,1))
