import styles from "./Post.module.css";

export default function Post() {
  return (
    <div className={styles.post}>
      <img
        className={styles.image}
        src="https://images.unsplash.com/photo-1473163928189-364b2c4e1135?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        alt=""
      />
      <div className={styles.info}>
        <div className={styles.categories}>
          <span className={styles.category}>Births</span>
          <span className={styles.category}>Warsaw</span>
        </div>
        <span className={styles.title}>Lorem ipsum dolor sit amet</span>
        <hr />
        <span className={styles.date}>1 hour ago</span>
      </div>
      <p className={styles.description}>
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Delectus,
        laudantium? Deserunt impedit illo recusandae labore possimus ratione
        aliquam quo ad. Tempora ratione blanditiis hic sequi eveniet pariatur
        tenetur vitae labore.
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Delectus,
        laudantium? Deserunt impedit illo recusandae labore possimus ratione
        aliquam quo ad. Tempora ratione blanditiis hic sequi eveniet pariatur
        tenetur vitae labore.  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Delectus,
        laudantium? Deserunt impedit illo recusandae labore possimus ratione
        aliquam quo ad. Tempora ratione blanditiis hic sequi eveniet pariatur
        tenetur vitae labore.  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Delectus,
        laudantium? Deserunt impedit illo recusandae labore possimus ratione
        aliquam quo ad. Tempora ratione blanditiis hic sequi eveniet pariatur
        tenetur vitae labore.
      </p>
    </div>
  );
}
