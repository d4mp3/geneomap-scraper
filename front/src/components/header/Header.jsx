import styles from "./Header.module.css"

export default function Header() {
    return (
        <div className={styles.header}>
                <span className={`${styles.titles} ${styles.title_lg}`}>Geneomap Blog</span>
                <span className={`${styles.titles} ${styles.title_sm}`}>JavaScript & Python </span>
        </div>
    )
}
