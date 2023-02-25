import { useContext, useEffect, useRef, useState } from 'react';
import AuthContext from './context/AuthProvider';

const LOGIN_URL = "/login";

const Login = () => {
  const { setAuth } = useContext(AuthContext);
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState('');
  const [pwd, setPwd] = useState('');
  const [errMsg, setErrMsg] = useState('');
  const [success, setSuccess] = useState(false);

  // set focus on username field
  useEffect(() => {
    userRef.current.focus();
  }, []);

  // if user retype username or pwd, clear error msg
  useEffect(() => {
    setErrMsg('');
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // SIMULATE SUCCESSFUL FAKE LOGIN
    setSuccess(true);

    // TRY REAL LOGIN 
    // try {
    //     const response = await axios.post(LOGIN_URL,
    //         JSON.stringify({ user: user, pwd: pwd }),
    //         {
    //             headers: { 'Content-Type': 'application/json' },
    //             withCredentials: true
    //         }
    //     );
    //     console.log(JSON.stringify(response?.data));
    //     const accessToken = response?.data?.accessToken;
    //     const roles = response?.data?.roles;
    //     setAuth({ user, pwd, roles, accessToken });
    //     setUser('');
    //     setPwd('');
    //     setSuccess(true);   // LOGIN SUCCESSFUL
    // } catch (err) {
    //     if (!err?.response) {
    //         setErrMsg('No Server Response');
    //     } else if (err.response?.status === 400) {
    //         setErrMsg('Missing Username or Password');
    //     } else if (err.response?.status === 401) {
    //         setErrMsg('Unauthorized');
    //     } else {
    //         setErrMsg('Login Failed');
    //     }
    //     errRef.current.focus();
    // }

    // If login fails, ask backend if they got enable CORS?
  };

  return (
    <>
      {success ? (
        <section>
          <h1>LOGIN SUCCESSFUL</h1>
          <h2>Insurance Home</h2>
          <p>Refresh to restart</p>
        </section>
      ) : (
        <section>
          {/* ERROR MSG */}
          <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"}>{errMsg}</p>
          <h1>Sign In</h1>
          <form onSubmit={handleSubmit}>

            {/* USERNAME FIELD */}
            <label htmlFor="employee">Employee id: </label>
            <input
              type="text"
              id="employee"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
            />


            {/* PASSWORD FIELD */}
            <label htmlFor="password">Password: </label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
            />

            {/* SIGN IN BUTTON */}
            <button>Sign In</button>
          </form>
        </section>
      )}
    </>
  )
}

export default Login