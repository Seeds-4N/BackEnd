import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { Link } from 'react-router-dom';
import styles from './CSS/signup.module.css';
import axios from 'axios';



const SignUp=(props)=>{
    const [name, setName] = useState(""); // 변수를 정의해야 함
    const [id, setId] = useState(""); // 변수를 정의해야 함
    const [password, setPassword] = useState(""); // 변수를 정의해야 함
    const [pwConfirm, setPwConfirm] = useState(""); // 변수를 정의해야 함
    

    const handleinputname=(e)=>{
        setName(e.target.value);
    };
    const handleinputid=(e)=>{
        setId(e.target.value);
    };
    const handleinputpw=(e)=>{
        setPassword(e.target.value);
    };
    const handleinputpwcfm=(e)=>{
        setPwConfirm(e.target.value);
    };

    const isvalidpassword=password.length>=8;
    const isvalidinput=name.length>=2;
    const isactive=isvalidpassword&&isvalidinput;
   
    const handleButtomValid = () => {
        if (
          !isvalidinput ||
          !isvalidpassword
          ) {
          alert('빈칸을 채워주세요.');
        }
        else{
            gotosignup();
        }
    };

    const gotosignup=()=>{
        const userData = {
            username: name,
            useremail: id,
            password: password,
            re_password: pwConfirm,
        };
       

        console.log("name:",name);
        console.log("id:",id);
        console.log("pw:",password);
        console.log("pwcfm:",pwConfirm);

        

        axios.post('http://127.0.0.1:8000/register/' ,userData
        //https://jsonplaceholder.typicode.com/todos/
        //http://127.0.0.1:8000/register/
        ,{
            name:name,
            id:id,
            password:password,
            re_password:pwConfirm,
        })
        .then((response)=>{
            console.log(response.data);
            alert('회원가입 성공');
        }).catch(error => {
            console.error(error);
        });
    };

    return (

        <body>
            <div>
                <div>회원가입</div>
                
                <input 
                    type="text"
                    id="name"
                    placeholder='이름을 입력해주세요'
                    required
                    value={name}
                    onChange={handleinputname}
                />
                
                <input
                    type='email'
                    id='id' 
                    placeholder='아이디를 입력해주세요'
                    required
                    value={id}
                    onChange={handleinputid}
                />
                
                <input
                    id='password'
                    type={'password'}
                    placeholder='비밀번호를 입력해주세요'
                    required
                    value={password}
                    onChange={handleinputpw}
                />
                
                <input
                    id='confirmpw'
                    type={'re_password'}
                    placeholder='비밀번호를 확인하세요.'
                    required
                    value={pwConfirm}
                    onChange={handleinputpwcfm}
                />
                <button className={isactive?'validbutton':'invalidbutton'} onClick={handleButtomValid}>회원가입</button>
                <div className='easy'>
                    <div>
                        google로 회원가입
                    </div>
                    <div>
                        kakao로 회원가입
                    </div>
                </div>
            </div>
        </body>
        
    )
    
};
export default SignUp;