import styles from "./Login.module.css";
import { Link } from "react-router-dom";

export default function Login() {
  return (
    <div className={styles.login}>
      <div className={styles.titles}>
        <span className={styles.title_lg}>Geneomap Blog</span>
          <span className={styles.title_sm}>JavaScript & Python </span>
      </div>
      <span className={styles.login_title}>Log in</span>
        <form className={styles.form}>
            <input className={styles.input} type="text" placeholder="Email adress"/>
            <input className={styles.input} type="password" placeholder="Password"/>
            <button className={styles.button}>Log in</button>
            <button className={styles.register_button}>
            <Link className="link" to="/register">Sign up</Link>
            </button>
        </form>
    </div>
  );
}