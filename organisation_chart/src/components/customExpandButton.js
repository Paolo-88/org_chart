import React from "react";
import { FaAngleDown, FaAngleUp } from "react-icons/fa";

const styles = {
  expandBtn: {
    width: "25px",
    height: "25px",
    margin: "auto",
    color: "#227c9d",
    backgroundColor: "#fef9ef",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    border: "2px solid #d3d3d3",
    borderRadius: "50%",
    cursor: "pointer",    
    position: "fixed", // Ensure it's positioned relatively within its container
    top: "25px", // Increase this value to move the icon lower
  },
  flex: {
    display: "flex",
  },
};

const CustomExpandButton = (node) => {
  return (
    <>
      {node && (
        <div style={styles.expandBtn}>
          <span>{node.data._directSubordinates}</span>
          <span style={styles.flex}>
            {node.children ? <FaAngleUp /> : <FaAngleDown />}
          </span>
        </div>
      )}
    </>
  );
};

export default CustomExpandButton;
