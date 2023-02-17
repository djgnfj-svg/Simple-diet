import { React, useState } from 'react'
import axios from "axios";
import { useNavigate } from 'react-router';

import './body_info_input.css';

function Body_info_input() {
  const navigate = useNavigate();
  const [userInput, setUserInput] = useState({
    age: "", // 나이
    height: "",  // 키
    weight: "",  // 몸무게
    gender: "",  // 성별
    general_activities: "", // 활동량
    excise_activity: "", // 운동량
  })
  const { age, height, weight, gender, general_activities, excise_activity } = userInput
  const handleChangeInput = (e) => {
    const { value, name } = e.target
    setUserInput({
      ...userInput,
      [name]: value
    })
  }
  const onkeytest = (e) => {
    if (e.target.value !== '') {
      e.target.classList.add('notEmpty');
    } else {
      e.target.classList.remove('notEmpty');
    }
  }
  const navigateToOutput = () => {
    axios.post("http://127.0.0.1:8000/api/cal-diet/", userInput)
      .then((e) => {
        navigate('/output', { state: e.data });
      })
      .catch((e) => {
        const error = e.response.data.error_msg
        console.log(e.response.data.error_msg)

        if (error.height == "A valid number is required.")
          alert("키를 입력해주세요")
        else if (error.height == "Ensure this value is less than or equal to 250.")
          alert("키는 140~250까지 입력가능합니다.")
        else if (error.height == "Ensure this value is greater than or equal to 140.")
          alert("키는 140~250까지 입력가능합니다.")
        // 몸무게
        else if (error.weight == "A valid number is required.")
          alert("몸무게를 입력해주세요")
        else if (error.weight == "Ensure this value is less than or equal to 250.")
          alert("몸무게는 40~250까지 입력가능합니다.")
        else if (error.weight == "Ensure this value is greater than or equal to 40.")
          alert("몸무게는 40~250까지 입력가능합니다.")
        // 나이
        else if (error.age == "A valid integer is required.")
          alert("나이를 입력해주세요")
        else if (error.age == "Ensure this value is less than or equal to 100.")
          alert("나이는 20~100까지 입력가능합니다")
        else if (error.age == "Ensure this value is greater than or equal to 20.")
          alert("나이는 20~100까지 입력가능합니다")
        // 체크박스
        else if (error.gender == 'This field may not be blank.')
          alert("성별을 선택해주세요")
        else if (error.general_activities == "A valid number is required.")
          alert("활동량을 입력해주세요")
        else if (error.excise_activity == "A valid number is required.")
          alert("운동량을 입력해 주세요")
        else if (error.diet_status == "This field is required.")
          alert("다이어트 여부를 선택해 주세요")
        else if (error.many_meals == "This field is required.")
          alert("몇끼를 드시는지 입력해 주세요")
      })
  }
  return (
    <header id="header" className="ex-2-header">
      <div className="container">
        <div className="row">
          <div className="col-lg-12">
            <h1>바디 정보</h1>
            <p>기초 대사량을 계산하여 알맞은 식단을 제공합니다.</p>
            <div className="form-container">
              <div>
                <div className="form-group">
                  <input name='height' onKeyUp={onkeytest} className="form-control-input"
                    onChange={handleChangeInput} value={height} required />
                  <label className="label-control" for="semail">키(cm)</label>
                  <div className="help-block with-errors"></div>
                </div>
                <div className="form-group">
                  <input name="weight" onKeyUp={onkeytest} type="text" className="form-control-input"
                    onChange={handleChangeInput} value={weight} required />
                  <label className="label-control" for="sname">몸무게(kg)</label>
                  <div on className="help-block with-errors"></div>
                </div>
                <div className="form-group">
                  <input name="age" onKeyUp={onkeytest} type="text" className="form-control-input"
                    onChange={handleChangeInput} value={age} required />
                  <label className="label-control" for="spassword">나이(만)</label>
                  <div className="help-block with-errors"></div>
                </div>
              </div>

              <div className="radio-group">
                <label className="label-text" for="gender">성별</label>
                <div class="wrapper">
                  <input type="radio" name="gender" id="option-1" onChange={handleChangeInput} value={"M"} />
                  <input type="radio" name="gender" id="option-2" onChange={handleChangeInput} value={"W"} />
                  <label for="option-1" class="option option-1">
                    <div class="dot"></div>
                    <span>남성</span>
                  </label>
                  <label for="option-2" class="option option-2">
                    <div class="dot"></div>
                    <span>여성</span>
                  </label>
                </div>

                <label className="label-text" for="ex">활동량</label>
                <div class="wrapper">
                  <input type="radio" name="general_activities" id="option-3" onChange={handleChangeInput} value={"1.2"} />
                  <input type="radio" name="general_activities" id="option-4" onChange={handleChangeInput} value={"1.4"} />
                  <input type="radio" name="general_activities" id="option-5" onChange={handleChangeInput} value={"1.6"} />
                  <label for="option-3" class="option option-3">
                    <div class="dot"></div>
                    <span>집이 최고</span>
                  </label>
                  <label for="option-4" class="option option-4">
                    <div class="dot"></div>
                    <span>평범</span>
                  </label>
                  <label for="option-5" class="option option-5">
                    <div class="dot"></div>
                    <span>활동적</span>
                  </label>
                </div>

                <label className="label-text" for="exs">운동량(주)</label>
                <div class="wrapper">
                  <input type="radio" name="excise_activity" id="option-6" onChange={handleChangeInput} value={"0"} />
                  <input type="radio" name="excise_activity" id="option-7" onChange={handleChangeInput} value={"0.1"} />
                  <input type="radio" name="excise_activity" id="option-8" onChange={handleChangeInput} value={"0.2"} />
                  <input type="radio" name="excise_activity" id="option-9" onChange={handleChangeInput} value={"0.3"} />
                  <label for="option-6" class="option option-6">
                    <div class="dot"></div>
                    <span>0회</span>
                  </label>
                  <label for="option-7" class="option option-7">
                    <div class="dot"></div>
                    <span>1~3회</span>
                  </label>
                  <label for="option-8" class="option option-8">
                    <div class="dot"></div>
                    <span>4~6회</span>
                  </label>
                  <label for="option-9" class="option option-9">
                    <div class="dot"></div>
                    <span>7+회</span>
                  </label>
                </div>
                <label className="label-text" for="diet_status">다이어트 여부</label>
                <div class="wrapper">
                  <input type="radio" name="diet_status" id="option-10" onChange={handleChangeInput} value={0.8} />
                  <input type="radio" name="diet_status" id="option-11" onChange={handleChangeInput} value={1.0} />
                  <label for="option-10" class="option option-10">
                    <div class="dot"></div>
                    <span>다이어트</span>
                  </label>
                  <label for="option-11" class="option option-11">
                    <div class="dot"></div>
                    <span>유지</span>
                  </label>
                </div>
              </div>
              <label className="label-text" for="many_meals">끼니</label>
              <div class="wrapper">
                <input type="radio" name="many_meals" id="option-12" onChange={handleChangeInput} value={2} />
                <input type="radio" name="many_meals" id="option-13" onChange={handleChangeInput} value={3} />
                <label for="option-12" class="option option-12">
                  <div class="dot"></div>
                  <span>2끼</span>
                </label>
                <label for="option-13" class="option option-13">
                  <div class="dot"></div>
                  <span>3끼</span>
                </label>
              </div>
              <div className="form-group">
                <button type="submit" className="form-control-submit-button"
                  onClick={navigateToOutput}>제출</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Body_info_input;
