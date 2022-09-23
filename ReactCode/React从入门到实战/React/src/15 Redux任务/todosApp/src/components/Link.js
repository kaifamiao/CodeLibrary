import React from 'react';
import PropTypes from 'prop-types';
// TODO: Link
const Link = ({ active, children, onClick }) => (
    <button
       onClick={onClick}
       disabled={active}
       style={{
           marginLeft: '4px'
       }}
    >
      {children}
    </button>
);
// TODO: Props Types
Link.propTypes = {
  active: PropTypes.bool.isRequired,
  children: PropTypes.node.isRequired,
  onClick: PropTypes.func.isRequired
}
// TODO: export
export default Link;
