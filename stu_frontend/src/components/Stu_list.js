

/////// change background color for individually each student component





import React, { useState, useEffect, useRef } from 'react';
import api from '../Api/Axios';

const Stu_item = React.lazy(() => import('./Stu_item'));

const Stu_list = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [renderCount, setRenderCount] = useState(0);
  const [clickedStudents, setClickedStudents] = useState(new Set()); // Use a Set to store clicked students
  const isMounted = useRef(false);

  useEffect(() => {
    api.get('/students/')
      .then(response => {
        setStudents(response.data);
        setLoading(false);
        setRenderCount(prevCount => prevCount + 1);
      })
      .catch(error => console.error('Error fetching students:', error));
  }, []);

  const handleStudentClick = (studentId) => {
    setClickedStudents(prevSet => new Set(prevSet).add(studentId)); // Add student ID to Set (no removal) and individual student click change bg : red again clk not change bg white 
  };
  return (
    <div style={{ padding: '20px', backgroundColor: 'white', minHeight: '100vh' }}>
      <h2>Student List</h2>

      {loading ? (
        <p>Loading students...</p>
      ) : (
        students.map(student => (
          <React.Suspense fallback={<p>Loading student...</p>} key={student.id}>
            <div 
              onClick={() => handleStudentClick(student.id)}
              style={{ 
                backgroundColor: clickedStudents.has(student.id) ? 'red' : 'white', // Change to red once clicked
                padding: '10px',
                border: '1px solid #ddd',
                margin: '10px 0',
                cursor: 'pointer',
                transition: 'background-color 0.3s ease'
              }}
            >
              <Stu_item student={student} />
            </div>
          </React.Suspense>
        ))
      )}

      <div
        style={{
          position: 'absolute',
          top: 10,
          right: 10,
          backgroundColor: '#f0f0f0',
          padding: '5px 10px',
          borderRadius: '5px',
        }}
      >
        Re-renders: {renderCount}
      </div>
    </div>
  );
};

export default Stu_list;

