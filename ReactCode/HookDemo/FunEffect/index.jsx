import React,{useState,useEffect} from "react";

function FunEffect(){
    const [count,setCount] = useState(0)
    
    useEffect(()=>{
        // document.title = `You clicked ${count} times`;
        console.log("执行了");
        return ()=>{
            console.log("销毁了");
        }
    },[])

    return (
      <div>
        <p>You clicked {count} times</p>
        <button onClick={() => setCount(count + 1)}>
          Click me
        </button>
      </div>
    );
}

export default FunEffect