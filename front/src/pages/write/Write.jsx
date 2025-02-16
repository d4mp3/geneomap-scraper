import styles from "./Write.module.css";

export default function Write() {
  return (
    <div className={styles.write}>
      <div className={styles.header}>
        <span className={styles.title_lg}>Geneomap Blog</span>
        <span className={styles.title_sm}>JavaScript & Python </span>
      </div>
      {/* <img
        className="image"
        src="https://images.unsplash.com/photo-1478860409698-8707f313ee8b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
        alt=""
      /> */}
      <form className={styles.form} action="">
        <div className={styles.form_group}>
          <label htmlFor="fileInput">
            <i className="icon fa-solid fa-plus"></i>
          </label>
          <input type="file" id="fileInput" style={{ display: "none" }} />
          <input
            type="text"
            placeholder="Title"
            className={styles.input}
            autoFocus={true}
          />
        </div>
        <div className={styles.form_group}>
          <textarea
            placeholder="What's Up, Doc?"
            type="text"
            className={`${styles.input} ${styles.text}`}
          ></textarea>
           <button className={styles.submit}>Publish post</button>
        </div>
      </form>

    </div>
  );
}
