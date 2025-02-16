import styles from "./Navbar.module.css";
import { Link } from "react-router-dom";

export default function NavBar() {
  const user = false;
  return (
    <div className={styles.nav}>
      <div className={styles.left}>
        <i className={`${styles.icon} fa-brands fa-square-gitlab`}></i>
        <i className={`${styles.icon} fa-brands fa-github`}></i>
        <i className={styles.left_info}>
          <Link className="link" to="/">about</Link>
        </i>
        <p className={styles.left_info}>|</p>
        <i className={styles.left_info}>
        <Link className="link" to="/">contact</Link>
          </i>
      </div>
      <div className={styles.center}>
        <ul className={styles.list}>
          <li className={styles.list_item}>
            <Link className="link" to="/">INDEX</Link>
          </li>
          <i className={styles.list_pipe}>|</i>
          <li className={styles.list_item}>BIRTHS</li>
          <li className={styles.list_item}>DEATHS</li>
          <li className={styles.list_item}>MARRIAGES</li>
          <i className={styles.list_pipe}>|</i>
          <li className={styles.list_item}>
          <Link className="link" to="/map">MAP</Link>
          </li>
          <i className={styles.list_pipe}>|</i>
          <li className={styles.list_item}>
          <Link className="link" to="/write">WRITE</Link>
          </li>
        </ul>
      </div>
      <div className={styles.right}>
      <i class={`${styles.search_icon} fa-solid fa-magnifying-glass`}></i>
        {
          user ? (
            <img
            className={styles.image}
            src="https://images.unsplash.com/photo-1595452767427-0905ad9b036d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
            alt=""
          />

          ) : (
            <ul className={styles.list}>
              <li className={styles.list_item}>
              <Link className={`link ${styles.login}`} to="/login">Log In</Link>
              </li>
              <li className={styles.list_pipe}>|</li>
              <li className={styles.list_item}>
              <Link className="link" to="/register">Sign Up</Link>
              </li>
            </ul>

          )

        }
        <p className={styles.logout}>
          {user && "Logout"}
            </p>
      </div>
    </div>
  );
}
