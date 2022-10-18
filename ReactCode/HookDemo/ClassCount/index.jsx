import React,{Component} from "react";

export default class ClassCount extends Component {
    constructor(props){
        super(props)
        this.state ={
            count : 0
        }
    }
    
    add=()=>{
        this.setState({
            count :this.state.count+1
        })
    }

    render(){
        return (
            <div>
                <p>你点击了{this.state.count}次</p>
                <button onClick={this.add}>点击+1</button>
            </div>
        )
    }
}