import Sidebar from "../../components/sidebar/Sidebar";
import styles from "./Settings.module.css";

export default function Settings() {
  return (
    <div className={styles.settings}>
      <div className={styles.wrapper}>
        <div className={styles.title}>
          <span className={styles.update_title}>Update Your Account</span>
          <span className={styles.delete_title}>Delete Account</span>
        </div>
        <form className={styles.form}>
          <label>Profile Picture</label>
          <div className={styles.profile_picture}>
            <img src="https://images.unsplash.com/photo-1523700664714-1345c3d6a0c1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt=""></img>
            <label htmlFor="fileInput">
              <i className={`${styles.profile_picture_icon} fa-solid fa-circle-user`}></i>
            </label>
            <input type="file" id="fileInput" style={{display:"none"}}/>
            </div>
            <label>Username</label>
            <input type="text" placeholder="d4mp3"/>
            <label>Email</label>
            <input type="email" placeholder="d4mp3@gmail.com"/>
            <label>Password</label>
            <input type="password"/>
            <button className={styles.submit}>Update</button>
        </form>
      </div>
    </div>
  );
}
