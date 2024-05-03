import { useRouter } from 'next/router';

export default function AnalysisPage() {
  const router = useRouter();
  const { website, data } = router.query;

  return (
    <div>
      <h1>Analysis Page for {website}</h1>
      <pre>{data}</pre>
    </div>
  );
}