import React, {Component} from 'react'
import PropTypes from 'prop-types'
import {CalculateType} from '../actions'

// TODO: HTML转义
function HTMLEncode(html) {
  var temp = document.createElement('div');
  (temp.textContent != null) ? (temp.textContent = html) : (temp.innerText = html);
  var output = temp.innerHTML;
  temp = null;
  return output;
}

// TODO: HTML反转义
function HTMLDecode(text) {
  var temp = document.createElement('div');
  temp.innerHTML = text;
  var output = temp.innerText || temp.textContent;
  temp = null;
  return output;
}

// TODO: define ES6 Class React Component
class CalculatorComp extends Component {
  // TODO: constructor
  constructor(props) {
    super(props);
    this.state = {
      b: 1
    };
    this.onNumClick = this.onNumClick.bind(this);
    this.onOprClick = this.onOprClick.bind(this);
    this.onEqualsClick = this.onEqualsClick.bind(this);
    this.onClsClick = this.onClsClick.bind(this);
  }

  // TODO: handle event
  onNumClick(e) {
    e.preventDefault();
    let n1, opr, n2, eq, result;
    if (this.state.b) {
      n1 = e.target.id.substr(3);
      n2 = this.props.vstore.getState().n2;
      opr = this.props.vstore.getState().opr;
      eq = this.props.vstore.getState().eq;
      result = this.props.vstore.getState().result;
      console.log('n1: ' + n1);
      console.log('n2: ' + n2);
      this.setState({
        b: 0
      });
    } else {
      n1 = this.props.vstore.getState().n1;
      n2 = e.target.id.substr(3);
      opr = this.props.vstore.getState().opr;
      eq = this.props.vstore.getState().eq;
      result = this.props.vstore.getState().result;
      console.log('n1: ' + n1);
      console.log('n2: ' + n2);
      this.setState({
        b: 1
      });
    }
    this.props.vstore.dispatch({
      type: CalculateType.NUM,
      n1: n1,
      n2: n2,
      opr: opr,
      eq: eq,
      result: result
    });
  }

  onOprClick(e) {
    e.preventDefault();
    let opr = e.target.id.toString();
    console.log('opr: ' + opr);
    this.props.vstore.dispatch({
      type: CalculateType.OPR,
      n1: this.props.vstore.getState().n1,
      n2: this.props.vstore.getState().n2,
      opr: opr,
      eq: this.props.vstore.getState().eq,
      result: this.props.vstore.getState().result
    });
  }

  onEqualsClick(e) {
    e.preventDefault();
    let eq = '=';
    console.log('eq: ' + eq);
    this.props.vstore.dispatch({
      type: CalculateType.EQUALS,
      n1: this.props.vstore.getState().n1,
      n2: this.props.vstore.getState().n2,
      opr: this.props.vstore.getState().opr,
      eq: eq,
      result: this.props.vstore.getState().result
    });
  }

  onClsClick(e) {
    e.preventDefault();
    this.props.vstore.dispatch({
      type: CalculateType.CLS,
      n1: '',
      n2: '',
      opr: '',
      eq: '',
      result: ''
    });
  }
  // TODO: render
  render() {
    // TODO: props
    const n1 = this.props.s.n1;
    const opr = this.props.s.opr;
    const n2 = this.props.s.n2;
    const eq = this.props.s.eq;
    const result = this.props.s.result;
    let lOpr;
    switch (opr) {
      case 'add':
        lOpr = '+';
        break;
      case 'minus':
        lOpr = '-';
        break;
      case 'multiple':
        lOpr = HTMLDecode('&#215;');
        console.log('multiple:' + lOpr);
        break;
      case 'divide':
        lOpr = HTMLDecode('&#247;');
        console.log('divide:' + lOpr);
        break;
      default:
        lOpr = '';
        break;
    }
    let expression = n1 + lOpr + n2 + eq + result;
    return (
      <span>
        <h3>基于React + Redux的简单计算器应用</h3>
        <p>计算结果: {expression}</p>
        <p>
        {' '}
        <button id='num1' onClick={this.onNumClick}> 1 </button>
        {' '}
        <button id='num2' onClick={this.onNumClick}> 2 </button>
        {' '}
        <button id='num3' onClick={this.onNumClick}> 3 </button>
        {' '}
        <button id='add' onClick={this.onOprClick}> + </button><br/>
        {' '}
        <button id='num4' onClick={this.onNumClick}> 4 </button>
        {' '}
        <button id='num5' onClick={this.onNumClick}> 5 </button>
        {' '}
        <button id='num6' onClick={this.onNumClick}> 6 </button>
        {' '}
        <button id='minus' onClick={this.onOprClick}> - </button><br/>
        {' '}
        <button id='num7' onClick={this.onNumClick}> 7 </button>
        {' '}
        <button id='num8' onClick={this.onNumClick}> 8 </button>
        {' '}
        <button id='num9' onClick={this.onNumClick}> 9 </button>
        {' '}
        <button id='multiple' onClick={this.onOprClick}> &#215; </button><br/>
        {' '}
        <button id='num0' onClick={this.onNumClick}> 0 </button>
        {' '}
        <button id='cls' onClick={this.onClsClick}> C </button>
        {' '}
        <button id='equal' onClick={this.onEqualsClick}> = </button>
        {' '}
        <button id='divide' onClick={this.onOprClick}> &#247; </button><br/>
        </p>
      </span>
    );
  }
}

// TODO: Props Type
CalculatorComp.propTypes = {
  result: PropTypes.string.isRequired,
  store: PropTypes.object
}
// TODO: export component
export default CalculatorComp;
