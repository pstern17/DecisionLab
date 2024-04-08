import React from 'react';
import './HomePage.css'
import Calendar from './Calendar.js'


function HomePage() {
  return (
    <div className= "hostpage">
    <p> PLAN AN EVENT</p>

      <Calendar></Calendar>

    </div>
  );
}

export default HomePage;
