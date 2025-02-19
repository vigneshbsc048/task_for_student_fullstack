////// change background color individually for each student component




import React, { useState, useEffect, useRef } from 'react';

const Stu_item = ({ student }) => {
  const [clickCount, setClickCount] = useState(0);
  const isRemounted = useRef(false);

  useEffect(() => {
    if (isRemounted.current) {
      setBackgroundColor("white");
    } else {
      isRemounted.current = true;
    }
  }, []);

  const [backgroundColor, setBackgroundColor] = useState("#fff");

  const handleStudentClick = () => {
    setClickCount((prevCount) => prevCount + 1);
  };

  return (
    <div>
      <h3>{student.name}</h3>
      <p>Age: {student.age}</p>
      <p>Grade: {student.grade}</p>
      <p>Clicks: {clickCount}</p>
      <button 
        onClick={handleStudentClick} 
        style={{ 
          padding: "5px 10px", 
          backgroundColor: "#007bff", 
          color: "white", 
          border: "none", 
          borderRadius: "5px", 
          cursor: "pointer"
        }}
      >
        Counter
      </button>
    </div>
  );
};

export default Stu_item;
