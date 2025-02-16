import styles from "./Home.module.css";
import Header from "../../components/header/Header";
import Posts from "../../components/posts/Posts";
import Sidebar from "../../components/sidebar/Sidebar";

export default function Home() {
  return (
    <>
      <Header/>
    <div className="home">
      <Posts/>
    </div>
    </>
  );
}
