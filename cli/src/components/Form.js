import React,{useState} from 'react'

function Form() {
    




    

 
  return (
    <div>
        <form  action = "http://localhost:5000/login" method = "post" className="form">
            <h1>Enter the patient vitals below</h1>
            <h2>Enter your Age</h2><br/>
            <input type="number" name="age" ></input><br/>
            <h2>Enter your restingbp</h2><br/>

            <input type="number" name="restingbp"></input><br/>
            <h2>Enter your maximum heartrate</h2><br/>

            <input type="number" name="maxhr" ></input><br/>
            <h2>Select your gender</h2><br/>

            <select name="gender" id="pet-select" ><br/>
\                <option value="1">Male</option>
                <option value="0.5">Female</option>
              
            </select>
            <h2>Enter you Bloodsugar level</h2><br/>

            <input type="number" name="fasting" ></input>
            <h2>Do you experience chest pain during physically intensive activites</h2><br/>

            <select name="exereciseangina" id="pet-select">
\                <option value="1">Yes</option>
                <option value="0">No</option>
              
            </select><br/>
            








            <input className='btn' type="submit" value="submit"/>
        </form>
    </div>
  )
}

export default Form