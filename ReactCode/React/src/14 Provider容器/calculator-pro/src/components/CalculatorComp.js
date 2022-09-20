import React, {Component} from 'react'
import PropTypes from 'prop-types'

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
    console.log("props:", props);
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
    let num = e.target.id.substr(3);
    console.log('num: ' + num);
    if (this.state.b) {
      this.props.onNumClick(num, this.props.n2, this.props.opr, this.props.eq, this.props.result);
      this.setState({
        b: 0
      });
    } else {
      this.props.onNumClick(this.props.n1, num, this.props.opr, this.props.eq, this.props.result);
      this.setState({
        b: 1
      });
    }
  }
  onOprClick(e) {
    e.preventDefault();
    let opr = e.target.id.toString();
    console.log('opr: ' + opr);
    this.props.onOprClick(this.props.n1, this.props.n2, opr, this.props.eq, this.props.result);
  }
  onEqualsClick(e) {
    e.preventDefault();
    let eq = '=';
    console.log('eq: ' + eq);
    console.log("props:", this.props);
    this.props.onEqualsClick(this.props.n1, this.props.n2, this.props.opr, eq, this.props.result);
  }
  onClsClick(e) {
    e.preventDefault();
    this.props.onClsClick(this.props.n1, this.props.n2, this.props.opr, this.props.eq, this.props.result);
  }
  // TODO: render
  render() {
    // TODO: props
    console.log("props:", this.props);
    const { n1, n2, opr, eq, result, onNumClick, onOprClick, onEqualsClick, onClsClick } = this.props;
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
      <h3>基于Provider的重构计算器应用</h3>
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
  result: PropTypes.number.isRequired,
  store: PropTypes.object
}
// TODO: export component
export default CalculatorComp;
