import React from 'react';
import ReactDOM from 'react-dom';
// TODO: define water temperature func Component
var divReact = document.getElementById('id-div-react');
// TODO: define ES6 Class Component
class WelcomeComp extends React.Component {
    // TODO: constructor
    constructor(props) {
        super(props);
    }
    // TODO: render
    render() {
        return <p>Hello, webpack+Babel+React!</p>;
    }
}
// TODO: render
ReactDOM.render(<WelcomeComp />, divReact);