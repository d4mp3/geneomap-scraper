import styles from "./Map.module.css";
import "leaflet/dist/leaflet.css";
import { MapContainer, TileLayer, ZoomControl, useMap, Marker, Popup } from "react-leaflet";
import Sidebar from "../../components/sidebar/Sidebar";

export default function Map() {
  return (
    <div className={styles.container}>
      <Sidebar/>
      <MapContainer className={styles.map} center={[51.505, -0.09]} zoom={13} zoomControl={false} scrollWheelZoom={true}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <ZoomControl position="bottomright"/>
      </MapContainer>
    </div>
  );
}
