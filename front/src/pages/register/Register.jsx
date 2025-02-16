import styles from "./Register.module.css";
import { Link } from "react-router-dom";

export default function Register() {
    return (
      <div className={styles.register}>
        <div className={styles.titles}>
            <span className={styles.title_lg}>Geneomap Blog</span>
            <span className={styles.title_sm}>JavaScript & Python </span>
        </div>
        <span className={styles.register_title}>Register</span>
          <form className={styles.form}>
            <input className={styles.input} type="text" placeholder="Username"/>
              <input className={styles.input} type="text" placeholder="Email adress"/>
              <input className={styles.input} type="password" placeholder="Password"/>
              <button className={styles.button}>Sign up</button>
              <button className={styles.login_button}>
              <Link className="link" to="/login">Log in</Link>
              </button>
          </form>
      </div>
    );
  }
