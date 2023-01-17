import { React, useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { useLocation, useNavigate } from 'react-router';


function Output_form() {
    const {state} = useLocation();


    return (
        <>
        <div>
            {alert("온겨?")}
            {console.log(state)}
        </div>
        </>
    )
}

export default Output_form;
