import Sidebar from "../../components/sidebar/Sidebar";
import SinglePost from "../../components/singlePost/SinglePost";
import styles from "./Single.module.css";

export default function Single() {
  return (
  <div className={styles.module}>
    <SinglePost/>
    <Sidebar/>
  </div>
  );
}
