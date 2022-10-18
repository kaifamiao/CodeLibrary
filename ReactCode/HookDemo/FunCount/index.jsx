import React,{useState} from "react";

function FunCount(){
    const [count,getCount] = useState(0)

    function add(){
        getCount(count+1)
    }

    return (
      <div>
        <p>你点击了{count}次</p>
        <button onClick={add}>点击+1</button>
      </div>
    );
}

export default FunCount