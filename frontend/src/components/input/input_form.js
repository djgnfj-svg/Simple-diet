import 'bootstrap/dist/css/bootstrap.min.css';
import './input_form.css';
import axios from "axios";

function Input_form() {
  const onkeytest = (e) => {
    if (e.target.value !== '') {
      e.target.classList.add('notEmpty');
    } else {
      e.target.classList.remove('notEmpty');
    }
  }
  return (
    <div className="">

      <header id="header" className="ex-2-header">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <h1>바디 정보</h1>
              <p>기초 대사량을 계산하여 알맞은 식단을 제공합니다.</p>
              <div className="form-container">
                <form id="signUpForm" data-toggle="validator" data-focus="false">
                  <div>

                    <div className="form-group">
                      <input onKeyUp={onkeytest} type="text" className="form-control-input" id="semail" required />
                      <label className="label-control" for="semail">키(cm)</label>
                      <div className="help-block with-errors"></div>
                    </div>
                    <div className="form-group">
                      <input onKeyUp={onkeytest} type="text" className="form-control-input" id="sname" required />
                      <label className="label-control" for="sname">몸무게(kg)</label>
                      <div className="help-block with-errors"></div>
                    </div>
                    <div className="form-group">
                      <input onKeyUp={onkeytest} type="text" className="form-control-input" id="spassword" required />
                      <label className="label-control" for="spassword">나이(만)</label>
                      <div className="help-block with-errors"></div>
                    </div>
                  </div>

                  <div className="radio-group">
                    <label className="label-text" for="gender">성별</label>
                    <div class="wrapper">
                      <input type="radio" name="select" id="option-1" />
                      <input type="radio" name="select" id="option-2" />
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
                      <input type="radio" name="select2" id="option-3"/>
                      <input type="radio" name="select2" id="option-4" />
                      <input type="radio" name="select2" id="option-5" />
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
                      <input type="radio" name="select3" id="option-6" />
                      <input type="radio" name="select3" id="option-7" />
                      <input type="radio" name="select3" id="option-8" />
                      <input type="radio" name="select3" id="option-9" />
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

                  </div>
                  <div className="form-group">
                    <button type="submit" className="form-control-submit-button"
                     onClick={()=>{
                      axios.post("http://127.0.0.1:8000/api/calk_metabolic_rate/").then((response)=>{
                        alert("성공")
                      })
                      .catch(()=>{
                        alert("실패")
                      })
                     }}>제출</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Input_form;
