import Post from "../post/Post";
import styles from "./Posts.module.css";


export default function Posts() {
  return (
  <div className={styles.posts}>
        <Post />
        <Post />
        <Post />
        <Post />
        <Post />
    </div>
  );
}
