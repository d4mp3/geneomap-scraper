import styles from "./SinglePost.module.css";

export default function SinglePost() {
  return (
    <div className={styles.single_post}>
      <div className={styles.wrapper}>
        <div className={styles.titles}>
          <span className={styles.title_lg}>Geneomap Blog</span>
          <span className={styles.title_sm}>JavaScript & Python </span>
        </div>
        <img
          src="https://images.unsplash.com/photo-1543191878-f6a3e470454e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
          className={styles.image}
        />
      </div>
      <h1 className={styles.post_title}>
        Lorem ipsum dolor sit amet.
        <div className={styles.edit}>
          <i className={`${styles.icon} fa-sharp fa-solid fa-user-pen`}></i>
          <i className={`${styles.icon} fa-regular fa-trash-can`}></i>
          <i class=""></i>
        </div>
      </h1>
      <div className={styles.info}>
        <span className={styles.author}>
          Autor: <b>NoName</b>
        </span>
        <span className={styles.author}>1 hour ago</span>
      </div>
      <p className={styles.description}>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Lectus urna duis
        convallis convallis tellus id interdum velit. Libero enim sed faucibus
        turpis in. Nisi lacus sed viverra tellus in hac habitasse platea
        dictumst. Dictum varius duis at consectetur. Libero enim sed faucibus
        turpis in eu mi bibendum. Orci dapibus ultrices in iaculis nunc sed.
        Risus nullam eget felis eget nunc. At erat pellentesque adipiscing
        commodo. Amet nulla facilisi morbi tempus iaculis urna. Id diam vel quam
        elementum pulvinar etiam non quam lacus. Eu augue ut lectus arcu
        bibendum at varius vel pharetra. Mi sit amet mauris commodo quis
        imperdiet. Interdum velit euismod in pellentesque massa placerat duis.
        Cum sociis natoque penatibus et magnis dis parturient montes nascetur.
        Pellentesque diam volutpat commodo sed egestas egestas fringilla.
        Pharetra sit amet aliquam id. In vitae turpis massa sed elementum. Enim
        facilisis gravida neque convallis a cras semper. Ante in nibh mauris
        cursus mattis molestie a iaculis at. Ipsum consequat nisl vel pretium
        lectus quam id leo in. Nisl pretium fusce id velit ut tortor pretium
        viverra. Augue ut lectus arcu bibendum at varius. Lectus urna duis
        convallis convallis tellus id interdum velit. Dictumst quisque sagittis
        purus sit amet volutpat consequat. Quam viverra orci sagittis eu
        volutpat odio facilisis. Accumsan in nisl nisi scelerisque eu. Convallis
        aenean et tortor at. Cras adipiscing enim eu turpis egestas pretium
        aenean pharetra magna. Sit amet porttitor eget dolor morbi non arcu. Vel
        pretium lectus quam id leo in vitae turpis. Risus pretium quam vulputate
        dignissim suspendisse in. Potenti nullam ac tortor vitae. Massa vitae
        tortor condimentum lacinia. Enim praesent elementum facilisis leo vel
        fringilla est ullamcorper eget. Tristique senectus et netus et
        malesuada. Ultricies leo integer malesuada nunc vel risus commodo
        viverra. Id diam maecenas ultricies mi eget mauris pharetra et ultrices.
        Ut etiam sit amet nisl. Dictum at tempor commodo ullamcorper a lacus
        vestibulum. Ultrices dui sapien eget mi proin sed libero enim sed. Eget
        nullam non nisi est. Tortor posuere ac ut consequat semper viverra.
        Egestas dui id ornare arcu odio. Nam libero justo laoreet sit.
        Pellentesque pulvinar pellentesque habitant morbi tristique senectus et.
        Ut faucibus pulvinar elementum integer enim neque volutpat ac tincidunt.
        Lectus vestibulum mattis ullamcorper velit sed. Aliquet bibendum enim
        facilisis gravida neque. Arcu ac tortor dignissim convallis aenean.
        Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat.
        Erat nam at lectus urna. Consequat nisl vel pretium lectus quam id.
        Lectus urna duis convallis convallis. Dictum at tempor commodo
        ullamcorper a. Sollicitudin nibh sit amet commodo nulla facilisi nullam
        vehicula ipsum. Tristique senectus et netus et malesuada fames ac turpis
        egestas. Id porta nibh venenatis cras. Sed pulvinar proin gravida
        hendrerit. Eget velit aliquet sagittis id consectetur purus ut faucibus.
        Mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Ut
        tellus elementum sagittis vitae et leo duis ut diam. Vestibulum rhoncus
        est pellentesque elit ullamcorper dignissim cras tincidunt. Blandit
        libero volutpat sed cras ornare arcu. Porttitor lacus luctus accumsan
        tortor posuere ac ut consequat semper. Purus sit amet luctus venenatis
        lectus magna fringilla urna porttitor. Sed blandit libero volutpat sed
        cras. Lectus proin nibh nisl condimentum. Egestas egestas fringilla
        phasellus faucibus scelerisque eleifend donec. Nec sagittis aliquam
        malesuada bibendum arcu vitae elementum. Libero volutpat sed cras ornare
        arcu. Proin libero nunc consequat interdum varius sit amet mattis
        vulputate. Vivamus arcu felis bibendum ut tristique. Tincidunt vitae
        semper quis lectus nulla at volutpat diam ut. Quis varius quam quisque
        id diam vel quam. Elit pellentesque habitant morbi tristique. Quis
        eleifend quam adipiscing vitae proin sagittis. Integer malesuada nunc
        vel risus commodo viverra maecenas accumsan.
      </p>
    </div>
  );
}
